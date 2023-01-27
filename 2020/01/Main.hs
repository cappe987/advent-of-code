module Main where

import Data.List
import Data.Maybe

solve_1 :: [Int] -> Int -> Int -> Int
solve_1 xs low high 
  | (xs !! low) + (xs !! high) > 2020 = solve_1 xs (low - 1) high
  | (xs !! low) + (xs !! high) < 2020 = solve_1 xs low (high + 1)
  | otherwise = (xs !! low) * (xs !! high)

-- Another version
solve_1' xs = head [a*b | a <- xs, b <- xs, a + b == 2020]

solve_2 :: [Int] -> Int
solve_2 xs = head [a*b*c | a <- xs, b <- xs, c <- xs, a + b + c == 2020]

main :: IO ()
main = do 
  contents <- readFile "input.txt"
  let xs = sort (map (\s -> read s :: Int) $ lines contents)
      start = fromJust (findIndex (> 1010) xs) 

  print $ solve_1 xs (start-1) start 
  print $ solve_2 xs