module Main where 

import Data.List
import Data.Maybe

createSums :: Int -> [Int] -> [(Int, Int, Int)]
createSums x = map (\x' -> (x,x', x+x'))

initSums :: [Int] -> [(Int, Int, Int)]
initSums [] = []
initSums (x:xs) = createSums x xs ++ initSums xs

removeSums :: Int -> [(Int, Int, Int)] -> [(Int, Int, Int)]
removeSums x = filter (\(a,b,_) -> x /= a && x /= b)

solve_1 :: [Int] -> [(Int, Int, Int)] -> [Int] -> Int
solve_1 (p:pre) sums (x:xs) = 
  case find (\(_,_,s) -> s == x) sums of
    Nothing -> x
    Just _  -> solve_1 (pre++[x]) (createSums x pre ++ removeSums p sums) xs

findContig :: [Int] -> Int -> Int -> Maybe [Int]
findContig (x:xs) goal acc  
  | newacc >  goal = Nothing
  | newacc == goal = Just [x]
  | otherwise = findContig xs goal newacc >>= \xs -> Just (x:xs)
  where newacc = x + acc

solve_2 :: [Int] -> Int -> [Int]
solve_2 xs goal = fromMaybe (solve_2 (tail xs) goal) (findContig xs goal 0)

main :: IO ()
main = do 
  input <- fmap (read :: String -> Int) . lines <$> readFile "input.txt" 
  let (preamble, rest) = splitAt 25 input

  let invalid = solve_1 preamble (initSums preamble) rest
  print invalid
  print $ (\xs -> minimum xs + maximum xs) $ solve_2 input invalid