module Main where

import Data.List
import Data.Maybe


---------------- Part 1 ----------------
parse :: [String] -> (Int, [Int])
parse [x,y] = (read x, map read $ filter (\a -> a /= "," && a /= "x") $ groupBy (\a b -> a /= ',' && b /= ',') y)

mapper :: Int -> Int -> (Int, Int)
mapper goal x = (x, x * ceiling (fromIntegral goal / fromIntegral x))

solve_1 :: Int -> [Int] -> Int
solve_1 goal input = 
  let (id, mins) = minimumBy (\(_,a) (_,b) -> compare a b) $ map (mapper goal) input
  in id * (mins-goal)


---------------- Part 2 ----------------
parse2 :: [String] -> [Maybe Int]
parse2 [_,y] = 
  map (\s -> if s=="x" then Nothing else Just (read s)) $ filter (/= ",") $ groupBy (\a b -> a /= ',' && b /= ',') y

solve_2 :: Int -> [Maybe Int] -> Int -> Int -> Int
solve_2 _ [] _ t = t
solve_2 jmp (Nothing:xs) i t = solve_2 jmp xs (i+1) t
solve_2 jmp (Just id:xs) i t = 
  solve_2 (jmp*id) xs (i+1) (timeStamp t)
  where timeStamp ac = if (ac+i) `mod` id /= 0 then timeStamp (ac+jmp) else ac

---------------- Main ----------------
main :: IO ()
main = do 
  (goal, input) <- parse . lines <$> readFile "input.txt"
  print $ solve_1 goal input

  input <- parse2 . lines <$> readFile "input.txt"
  print $ solve_2 (fromJust $ head input) (tail input) 1 0
