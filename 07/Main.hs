module Main where

import Data.List
import Data.Function
import Data.Bifunctor as Bf
import Prelude as P
import Data.Maybe

parseContains :: [String] -> [(String, Int)]
parseContains (num:v1:v2:ws) = 
  (color, amount) : parseContains (P.drop 1 ws)
  where color = if num == "no" then "" else v1 ++ v2
        amount = if num == "no" then 0 else read num
parseContains _ = []

parseLine :: String -> (String, [(String, Int)])
parseLine s = 
  (color, contains')
  where ws = words s
        color = head ws ++ (ws !! 1)
        contains = parseContains (P.drop 4 ws)
        contains' = case contains of [("", 0)] -> []; xs -> xs;

parse :: [String] -> [(String, [(String, Int)])]
parse = P.map parseLine

canContain :: String -> [(String, [String])] -> [(String, [String])]
canContain color input = 
  if P.null contains then
    []
  else
    contains ++ P.foldl (\acc cont -> acc ++ canContain (fst cont) input) [] contains
  where contains = P.filter (\(_, xs) -> color `elem` xs) input
  
countContainers :: (String, Int) -> [(String, [(String, Int)])] -> Int
countContainers (color, num) input = 
  num + num * insideOne
  where (_, inside) = fromJust $ find (\(s,_) -> s == color) input
        insideOne = P.foldl (\acc c -> acc + countContainers c input) 0 inside

main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"

  -- Part 1
  print $ length $ nub $ fmap fst $ canContain "shinygold" $ Bf.second (fmap fst) <$> parse input

  -- Part 2
  print $ countContainers ("shinygold", 1) (parse input) - 1