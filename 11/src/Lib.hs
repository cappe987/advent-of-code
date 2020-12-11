{-# LANGUAGE BangPatterns #-}
module Lib
    ( m
    ) where

import Data.List
import qualified Data.Map.Strict as Map
import Data.Array
import Data.Time

type Point = (Int, Int)

type Statecheck = Array Point Char -> (Point, Char) -> Maybe Char

type Grid = Map.Map Point Char

adjacent :: Point -> [Point]
adjacent (y,x) = 
  [(y+1,x+1), (y+1, x), (y+1,x-1), (y,x+1), (y, x-1), (y-1, x-1), (y-1, x), (y-1, x+1)]

count :: Eq a => a -> [a] -> Int
count c = length . filter (== c)

inboundsArr :: Point -> Point -> Bool
inboundsArr (by, bx) (y,x) = y >= 0 && y <= by && x >= 0 && x <= bx

getNeighbours :: Point -> Array Point Char -> String
getNeighbours pos grid = 
  (grid !) <$> adj
  where adj = filter (inboundsArr (snd $ bounds grid)) $ adjacent pos 

stateCheck :: Statecheck
stateCheck grid (pos, c) 
  | c == '#' && count '#' adj > 3  = Just 'L'
  | c == 'L' && count '#' adj == 0 = Just '#'
  | otherwise = Nothing
  where adj = getNeighbours pos grid

linearTraverse :: Point -> Array Point Char -> Point -> Char
linearTraverse (y,x) grid (dy,dx) 
  | not $ inboundsArr (snd $ bounds grid) newpoint = '.'
  | grid ! newpoint == '.' = linearTraverse newpoint grid (dy,dx)
  | otherwise = grid ! newpoint
  where newpoint = (y+dy, x+dx) 

stateCheck2 :: Statecheck
stateCheck2 grid (pos, c) 
  | c == '#' && count '#' adj > 4  = Just 'L'
  | c == 'L' && count '#' adj == 0 = Just '#'
  | otherwise = Nothing
  where adj = linearTraverse pos grid <$> dirs
        dirs = [(1,1), (1,0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

updateCell :: Statecheck -> Array Point Char -> Grid -> Point -> Char -> Grid
updateCell check orig acc p c = 
  case check orig (p,c) of
    Nothing -> acc
    Just c' -> Map.adjust (const c') p acc

mapToMatrix :: Grid -> Point -> Array Point Char
mapToMatrix m size = 
  listArray ((0,0), size) 
    $ concatMap (fmap snd) $ groupBy (\((a,_), _) ((b,_), _) -> a == b) $ Map.toAscList m

generation :: Statecheck -> Grid -> Point -> Grid
generation check grid size = 
  if grid == newgrid then grid else generation check newgrid size
  where newgrid = Map.foldlWithKey' (updateCell check (mapToMatrix grid size)) grid grid

parse :: [String] -> (Grid, Point)
parse ss = 
  (Map.fromAscList $ zip points (concat ss), (length ss - 1, length (head ss) - 1))
  where points = [(y,x) | y <- [0..length ss - 1], x <- [0..length (head ss)-1]]

m :: IO ()
m = do
  (grid, arrbounds) <- parse . lines <$> readFile "src/input.txt"
  
  time $ count '#' $ map snd $ Map.toList $ generation stateCheck grid arrbounds
  time $ count '#' $ map snd $ Map.toList $ generation stateCheck2 grid arrbounds

time :: Int -> IO ()
time a = do
    start <- getCurrentTime
    let !v = a 
    end <- getCurrentTime
    let diff = diffUTCTime end start
    print $ nominalDiffTimeToSeconds diff
    print v