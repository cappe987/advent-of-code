module Main where

countTrees :: [(Int, Int)] -> Int -> [String] -> Int
countTrees [] _ _ = 0
countTrees ((line, col):cs) end xs 
  | (xs !! line) !! col == '#' = 1 + countTrees cs end xs
  | otherwise                  =     countTrees cs end xs

-- Generate a list of coordinates to travel
coordinates :: Int -> Int -> Int -> Int -> [(Int, Int)]
coordinates linestep colstep wrap end = 
  getcoords (0,0)
  where getcoords (line, _  ) | line + linestep >= end = []
        getcoords (line, col) = 
          (line + linestep, (col + colstep) `mod` wrap) : getcoords (line + linestep, col + colstep)

solve_1 :: [String] -> IO ()
solve_1 input = do
  let end = length input
      wrap = length (head input) 
  print $ countTrees (coordinates 1 3 wrap end) end input

solve_2 :: [String] -> IO ()
solve_2 input = do
  let end = length input
      wrap = length (head input) 
      coords = [(1,1), (1,3), (1,5), (1,7), (2,1)]

  print $ foldl (\acc (l,c) -> acc * countTrees (coordinates l c wrap end) end input) 1 coords

main :: IO () 
main = do 
  input <- lines <$> readFile "input.txt"
  solve_1 input
  solve_2 input
