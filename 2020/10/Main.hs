module Main where

import Data.List

solve_1 :: [Int] -> (Int, Int) -> (Int, Int)
solve_1 (x:y:xs) (a,b) 
  | y-x == 3 = solve_1 (y:xs) (a,b+1)
  | y-x == 2 = solve_1 (y:xs) (a,b  )
  | y-x == 1 = solve_1 (y:xs) (a+1,b)
solve_1 _ (a,b) = (a, b+1)


fillzero :: [Int] -> [Int]
fillzero [x] = [x]
fillzero (x:y:xs) = x : replicate (y-x-1) 0 ++ fillzero (y:xs)

solve_2 :: [Int] -> [Int] -> Int
solve_2 vals [_] = sum vals
solve_2 vals (0:xs) = solve_2 (tail vals ++ [0]) xs
solve_2 vals (_:xs) = 
  let val = sum vals
  in solve_2 (tail vals ++ [val]) xs


main :: IO ()
main = do
  input <- fmap (read :: String -> Int) . lines <$> readFile "input.txt"
  print $ uncurry (*) $ solve_1 (0:sort input) (0,0) 
  print $ solve_2 [0,0,1] (fillzero $ sort input)