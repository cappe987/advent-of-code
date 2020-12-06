module Main where


import Data.List

parse :: String -> [[String]]
parse s = filter (/= [""]) $ groupBy (\a b -> a /= "" && b /= "") $ lines s

solve_1 :: [String] -> Int
solve_1 = foldl (\acc x -> acc + length (nub x)) 0

solve_2 :: [[String]] -> Int
solve_2 = foldl (\acc x -> acc + length (foldl1 intersect x)) 0

main :: IO ()
main = do 
  input <- readFile "input.txt"
  print $ solve_1 $ map concat $ parse input
  print $ solve_2 $ parse input