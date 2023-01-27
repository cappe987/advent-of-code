module Main where

type Boat = ((Int, Int), (Int, Int))

------------- Part 1 ----------------
moveForward :: Boat -> Int -> Boat
moveForward (p, (dx,dy)) n = (foldl (\(x, y) _ -> (x+dx, y+dy)) p [1..n], (dx,dy))

turnLeft :: Boat -> Int -> Boat
turnLeft  (p, (dx,dy)) n = if n == 0 then (p, (dx,dy)) else turnLeft  (p, (dy, -dx)) (n-1)

turnRight :: Boat -> Int -> Boat
turnRight (p, (dx,dy)) n = if n == 0 then (p, (dx,dy)) else turnRight (p, (-dy, dx)) (n-1)

moveDir :: (Int, Int) -> Boat -> Int -> Boat
moveDir (dx,dy) ((x,y), d) n = 
  if n == 0 then ((x,y), d) else moveDir (dx, dy) ((x+dx, y+dy), d) (n-1)

solve_1 :: [String] -> Boat -> Int
solve_1 [] ((x,y), _) = abs x + abs y
solve_1 (('F':n):xs) boat = solve_1 xs (moveForward boat (read n))
solve_1 (('L':n):xs) boat = solve_1 xs (turnLeft  boat (read n `div` 90))
solve_1 (('R':n):xs) boat = solve_1 xs (turnRight boat (read n `div` 90))
solve_1 (('N':n):xs) boat = solve_1 xs (moveDir ( 0,-1) boat (read n))
solve_1 (('S':n):xs) boat = solve_1 xs (moveDir ( 0, 1) boat (read n))
solve_1 (('E':n):xs) boat = solve_1 xs (moveDir ( 1, 0) boat (read n))
solve_1 (('W':n):xs) boat = solve_1 xs (moveDir (-1, 0) boat (read n))


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

------------- Main ----------------
main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"
  
  print $ solve_1 input ((0,0), (1,0))
  print $ solve_2 input (0,0) (10, -1)
