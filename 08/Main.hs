module Main where

import Data.Maybe
import Data.List

parseLine :: String -> (String, Int)
parseLine s = 
  let ws = words s
  in (head ws, read (filter (/= '+') (ws !! 1)))

parse :: [String] -> [(String, Int)]
parse = map parseLine 


executeInf :: [(String, Int)] -> [Int] -> Int -> Int -> Int
executeInf xs visited i acc
  | i `elem` visited = acc
  | op == "nop" = executeInf xs (i:visited) (i+1) acc
  | op == "jmp" = executeInf xs (i:visited) (i+val) acc
  | op == "acc" = executeInf xs (i:visited) (i+1) (acc + val)

  where (op, val) = xs !! i

execute :: [(String, Int)] -> Int -> [Int] -> Int -> Int -> Maybe Int
execute xs i visited end acc 
  | i == end = Just acc
  | i `elem` visited = Nothing
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

  print $ executeInf (parse input) [] 0 0
  let instr = parse input
  let res = find (\xs -> isJust $ execute xs 0 [] (length instr) 0) $ replaceAll instr []
  print $ fromJust $ execute (fromJust res) 0 [] (length instr) 0