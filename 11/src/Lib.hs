module Lib
    ( m
    ) where

import Data.List
-- import Data.Function.Memoize
import Data.Maybe
import qualified Data.Map.Strict as Map
import Data.Array
import Data.Bifunctor as Bf

type Point = (Int, Int)

-- data State = Empty | Occupied deriving (Eq, Show)

type Grid = Map.Map Point Char

adjacent (y,x) = 
  [(y+1,x+1), (y+1, x), (y+1,x-1), (y,x+1), (y, x-1), (y-1, x-1), (y-1, x), (y-1, x+1)]

count c = length . filter (== c)

getNeighbours :: Point -> Map.Map Point Char -> String
getNeighbours pos g = 
  foldl (\acc x -> if isJust x then fromJust x : acc else acc) [] 
    $ (`Map.lookup` g) <$> adjacent pos

state :: Map.Map Point Char -> (Point, Char) -> Maybe Char
state grid (pos, c) 
  | c == '#' && count '#' adj > 3  = Just 'L'
  | c == 'L' && count '#' adj == 0 = Just '#'
  | otherwise = Nothing
  where adj = getNeighbours pos grid

parse :: [String] -> Grid
parse ss = 
  Map.fromAscList $ filter (\(_,c) -> c /= '.') $ zip points (concat ss) 
  -- Map.fromAscList $ zip points (concat ss) 
  where points = [(y,x) | y <- [0..length ss - 1], x <- [0..length (head ss)-1]]

updateCell orig acc p c = 
  case state orig (p,c) of
    Nothing -> acc
    Just c' -> Map.adjust (const c') p acc

-- generation :: Grid -> Int -> Int
generation grid = 
  if grid == newgrid then grid else generation newgrid
  where newgrid = Map.foldlWithKey' (updateCell grid) grid grid


m :: IO ()
m = do

  input <- parse . lines <$> readFile "src/input.txt"
  
  -- print input
  print $ count '#' $ map snd $ Map.toList $ generation input
  
  putStrLn ""
