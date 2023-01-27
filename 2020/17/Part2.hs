module Main where

import Data.List
import Data.Array
import Data.Array.MArray
import Data.Array.IO
import Data.Foldable
import Control.Monad

type Point = (Int, Int, Int, Int)

sumTuple :: Point -> Point -> Point
sumTuple (w1, z1,y1,x1) (w2, z2,y2,x2) = (w1+w2, z1+z2, y1+y2, x1+x2)

dirs :: [Point]
dirs = [(w, z,y,x) | w <- [-1..1], z <- [-1..1], y <- [-1..1], x <- [-1..1], (w,z,y,x) /= (0,0,0,0)]

neighbours :: Point -> [Point]
neighbours p = map (sumTuple p) dirs

count :: Char -> String -> Int
count x = length . filter (==x)

newState :: Array Point Char -> Point -> Maybe Char
newState arr pos = 
  let alive = count '#' $ map (arr !) $ neighbours pos
      curr   = arr ! pos
  in 
    if curr == '#' && (alive > 3 || alive < 2) then Just '.'
    else if curr == '.' && alive == 3 then Just '#'
    else Nothing

  
update :: Array Point Char -> IOUArray Point Char -> Point -> IO ()
update immutarr mutarr p = 
  forM_ (newState immutarr p) (writeArray mutarr p)

pointsBetween :: Point -> Point -> [Point]
pointsBetween (lw, lz,ly,lx) (uw, uz,uy,ux) = 
  [(w, z,y,x) | w <- [lw..uw], z <- [lz..uz], y <- [ly..uy], x <- [lx..ux]]

generation :: IOUArray Point Char -> IO ()
generation mutarr = do 
  immutarr <- freeze mutarr 

  let (l,u) = bounds immutarr
  
  mapM_ (update immutarr mutarr) $ pointsBetween (sumTuple (1,1,1,1) l) (sumTuple (-1,-1,-1,-1) u)


countAlive :: Array Point Char -> Int
countAlive immutarr = 
  let (l,u) = bounds immutarr

  in foldl (\acc p -> if immutarr ! p == '#' then acc+1 else acc) 0 $ pointsBetween (sumTuple (1,1,1,1) l) (sumTuple (-1,-1,-1,-1) u)

main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt" -- Part 2: 2400
  let c = 7
      width  = length (head input) + 1
      height = length input + 1

  -- Using (w,z,y,x) format since that makes it print correctly
  mutarr <- newArray ((-c,-c,-c,-c), (c, c,height+c,width+c)) '.' :: IO (IOUArray Point Char)

  let init = [(e, (x,y)) | (y,es) <- zip [0..] input, (x,e) <- zip [0..] (input !! y)]
  mapM_ (\(e, (x,y)) -> writeArray mutarr (0, 0, y, x) e) init

  replicateM_ 6 (generation mutarr)

  immutarr <- freeze mutarr :: IO (Array Point Char)
  -- print immutarr
  print $ countAlive immutarr