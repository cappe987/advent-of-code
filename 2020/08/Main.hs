module Main where

import Data.Maybe
import Data.Either
import Data.List

parseLine :: String -> (String, Int)
parseLine s = 
  let ws = words s
  in (head ws, read (filter (/= '+') (ws !! 1)))

parse :: [String] -> [(String, Int)]
parse = map parseLine 

execute :: [(String, Int)] -> Int -> [Int] -> Int -> Int -> Either Int Int
execute xs i visited end acc 
  | i == end = Right acc
  | i `elem` visited = Left acc
  | op == "nop" = execute xs (i+1) (i:visited) end acc
  | op == "jmp" = execute xs (i+val) (i:visited) end acc
  | op == "acc" = execute xs (i+1) (i:visited) end (acc+val)
  where (op, val) = xs !! i

replaceAll :: [(String, Int)] -> [(String, Int)] -> [[(String, Int)]]
replaceAll xs acc 
  | null xs = []
  | op == "nop" = (reverse (("jmp", val):acc)++tail xs) : replaceAll (tail xs) ((op,val):acc)
  | op == "jmp" = (reverse (("nop", val):acc)++tail xs) : replaceAll (tail xs) ((op,val):acc)
  | otherwise = replaceAll (tail xs) ((op,val):acc)
  where (op, val) = head xs

main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"

  let instr = parse input
      len   = length instr
  print $ fromLeft 0 $ execute instr 0 [] len 0

  let res = find (\xs -> isRight $ execute xs 0 [] len 0) $ replaceAll instr []
  print $ fromRight 0 $ execute (fromJust res) 0 [] len 0