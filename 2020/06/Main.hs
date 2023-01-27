module Main where


import Data.List

parse :: String -> [[String]]
parse s = filter (/= [""]) $ groupBy (\a b -> a /= "" && b /= "") $ lines s

solve_1 :: [String] -> Int
solve_1 = foldl (\acc x -> acc + length (nub x)) 0

solve_2 :: [[String]] -> Int
solve_2 = foldl (\acc x -> acc + length (foldl1 intersect x)) 0


solve_1_1 = print . foldl (\acc x -> acc + length (nub x)) 0 . map concat . filter (/= [""]) . groupBy (\a b -> a /= "" && b /= "") . lines =<< readFile "input.txt"

solve_1_2 = print . foldl (\acc x -> acc + length (foldl1 intersect x)) 0 . filter (/= [""]) . groupBy (\a b -> a /= "" && b /= "") . lines =<< readFile "input.txt"

main :: IO ()
main = do 
  input <- readFile "input.txt"
  print $ solve_1 $ map concat $ parse input
  print $ solve_2 $ parse input

  solve_1_1 
  solve_1_2