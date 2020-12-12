module Main where


data Instruction = F Int | D Dir Int | L Int | R Int deriving Show

data Dir = East | West | South | North deriving Show

data Boat = Boat Dir (Int, Int) deriving Show

turnRight boat degrees = foldl turn boat [1..degrees `div` 90]
  where turn (Boat East  p) _ = Boat South p
        turn (Boat South p) _ = Boat West p
        turn (Boat West  p) _ = Boat North p
        turn (Boat North p) _ = Boat East p

turnLeft boat degrees = foldl turn boat [1..degrees `div` 90]
  where turn (Boat East  p) _ = Boat North p
        turn (Boat South p) _ = Boat East p
        turn (Boat West  p) _ = Boat South p
        turn (Boat North p) _ = Boat West p

moveForward (Boat East  (x,y)) n = Boat East  (x+n, y)
moveForward (Boat South (x,y)) n = Boat South (x, y+n)
moveForward (Boat West  (x,y)) n = Boat West  (x-n, y)
moveForward (Boat North (x,y)) n = Boat North (x, y-n)

moveDir (Boat d (x,y)) East  n = Boat d (x+n,y)
moveDir (Boat d (x,y)) South n = Boat d (x,y+n)
moveDir (Boat d (x,y)) West  n = Boat d (x-n,y)
moveDir (Boat d (x,y)) North n = Boat d (x,y-n)

parse :: [String] -> [Instruction]
parse = 
  fmap parseLine 
  where parseLine ('F':xs) = F (read xs)
        parseLine ('N':xs) = D North (read xs)
        parseLine ('S':xs) = D South (read xs)
        parseLine ('W':xs) = D West  (read xs)
        parseLine ('E':xs) = D East  (read xs)
        parseLine ('L':xs) = L (read xs)
        parseLine ('R':xs) = R (read xs)

solve_1 [] (Boat _ (x,y)) = abs x + abs y
solve_1 (F n:xs) boat = solve_1 xs (moveForward boat n)
solve_1 (L n:xs) boat = solve_1 xs (turnLeft  boat n)
solve_1 (R n:xs) boat = solve_1 xs (turnRight boat n)
solve_1 (D d n:xs) boat = solve_1 xs (moveDir boat d n)


------------- Part 2 ----------------
moveBoat :: (Int, Int) -> (Int, Int) -> Int -> (Int, Int)
moveBoat boat wp n = foldl (\(a,b) (x, y) -> (a+x, b+y)) boat (replicate n wp)

rotateRight :: (Int, Int) -> Int -> (Int, Int)
rotateRight (px,py) n = if n == 0 then (px,py) else rotateRight (-py, px) (n-1)

rotateLeft :: (Int, Int) -> Int -> (Int, Int)
rotateLeft (px,py) n = if n == 0 then (px,py) else rotateLeft (py, -px) (n-1)

solve_2 :: [String] -> (Int, Int) -> (Int, Int) -> Int
solve_2 [] (x,y) _                 = x+y
solve_2 (('F':n):xs) boat wayp     = solve_2 xs (moveBoat boat  wayp (read n)) wayp
solve_2 (('L':n):xs) boat wayp     = solve_2 xs boat (rotateLeft  wayp (read n `div` 90))
solve_2 (('R':n):xs) boat wayp     = solve_2 xs boat (rotateRight wayp (read n `div` 90))
solve_2 (('N':n):xs) boat (px, py) = solve_2 xs boat (px, py - read n)
solve_2 (('S':n):xs) boat (px, py) = solve_2 xs boat (px, py + read n)
solve_2 (('W':n):xs) boat (px, py) = solve_2 xs boat (px - read n, py)
solve_2 (('E':n):xs) boat (px, py) = solve_2 xs boat (px + read n, py)

main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"
  
  -- print input
  print $ solve_1 (parse input) (Boat East (0,0))
  print $ solve_2 input (0,0) (10, -1)
  putStrLn ""
