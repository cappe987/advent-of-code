module Main where

import Data.Char
import Data.Function
import Data.Bifunctor as Bf

parse :: String -> ([Int], Char, String)
parse s = 
  ([read lower, read upper], char, pass)
  where parts = words s
        (lower, r) = span isDigit (head parts)
        upper = tail r
        char = head $ head (tail parts)
        pass = parts !! 2


-- One-liner for parsing and running the solve function.
parse' :: (([Int], Char, String) -> Bool) -> IO Int
parse' solve = 
  (length . filter (== True)) . fmap (\w -> solve (read <$> (span isDigit (head w) & (\(l,r) -> [l,tail r])), head (w !! 1), w !! 2)) <$> (map words . lines <$> readFile "input.txt")

isValid_1 ([l, u], c, pass) = 
  length (filter (== c) pass) `elem` [l..u]

isValid_2 ([l, u], c, pass) = 
  if lc == c then uc /=c else uc == c
  where lc = pass !! (l-1)
        uc = pass !! (u-1)

main :: IO ()
main = do 
  parse' isValid_1 >>= print
  parse' isValid_2 >>= print

  -- input <- fmap parse . lines <$> readFile "input.txt" 
  -- print $ length (filter isValid_1 input)
  -- print $ length (filter isValid_2 input)