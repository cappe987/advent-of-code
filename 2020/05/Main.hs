module Main where

import Data.List
import Data.Bool

bsearch [] l _ = l
bsearch ('F' : xs) l u = bsearch xs l ((l + u) `div` 2)
bsearch ('B' : xs) l u = bsearch xs ((l + u) `div` 2 + 1) u
bsearch ('L' : xs) l u = bsearch xs l ((l + u) `div` 2)
bsearch ('R' : xs) l u = bsearch xs ((l + u) `div` 2 + 1) u

seatId x =
  let (r, c) = splitAt 7 x
  in bsearch r 0 127 * 8 + bsearch c 0 7

solve_1 = maximum . map seatId

solve_2 lines = 
  let seatIds = sort $ map seatId lines
  in 1 + foldl (\p a -> bool p a (p==a-1)) (head seatIds) seatIds

main = do
  input <- lines <$> readFile "input.txt"

  print $ solve_1 input
  print $ solve_2 input