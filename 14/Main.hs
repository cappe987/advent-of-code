module Main where

import Data.Bits
import qualified Data.Map as Map

type Bitflip      = Int -> Int
type FloatAddress = Int -> [Int]
type Mask         = ([Bitflip], [FloatAddress]) 
type MaskParser   = Int -> String -> Mask -> Mask
type Memory       = Map.Map Int Int

data Op = Asn Int Int | Mask Mask


------------------ Part 1 --------------------
parseMask :: MaskParser
parseMask _ [] mask = mask
parseMask pow ('0':xs) (a,b) = parseMask (pow+1) xs ((complement (2^pow) .&.):a,b)
parseMask pow ('1':xs) (a,b) = parseMask (pow+1) xs (((2^pow) .|.):a,b)
parseMask pow ('X':xs) (a,b) = parseMask (pow+1) xs (a,b)

solve_1 :: [Op] -> [Bitflip] -> Memory -> Int
solve_1 [] _ mem = sum $ map snd $ Map.toList mem
solve_1 (Mask (bflips,_) : xs) _ mem = solve_1 xs bflips mem
solve_1 (Asn a b : xs) mask mem = 
  solve_1 xs mask (Map.insert a (foldl (flip ($)) b mask) mem)



------------------ Part 2 --------------------
writeFloating :: Int -> Int -> [Int]
writeFloating pow i = [complement (2^pow) .&. i, (2^pow) .|. i]

parseMask2 :: MaskParser
parseMask2 _   [] mask = mask
parseMask2 pow ('0':xs) mask  = parseMask2 (pow+1) xs mask
parseMask2 pow ('1':xs) (a,b) = parseMask2 (pow+1) xs (((2^pow) .|.):a, b)
parseMask2 pow ('X':xs) (a,b) = parseMask2 (pow+1) xs (a, writeFloating pow : b)

solve_2 :: [Op] -> Mask -> Memory -> Int
solve_2 [] _ mem = sum $ map snd $ Map.toList mem
solve_2 (Mask mask : xs) _ mem = solve_2 xs mask mem
solve_2 (Asn a b   : xs) (bflips, floats) memory = 
  solve_2 xs (bflips, floats) $ foldl (flip (`Map.insert` b)) memory addrs
  where addr = foldl (flip ($)) a bflips
        addrs = foldl (>>=) [addr] floats


------------------ Main --------------------
parseOp :: MaskParser -> String -> Op
parseOp parser s = 
  if head ws == "mask" then
    Mask $ parser 0 (reverse $ ws !! 2) ([],[])
  else
    Asn (read $ takeWhile (/= ']') $ drop 4 (head ws)) (read (ws !! 2))
  where ws = words s
  
main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"
  let ops1 = map (parseOp parseMask ) input
      ops2 = map (parseOp parseMask2) input

  print $ solve_1 (tail ops1) ((\(Mask m) -> fst m) $ head ops1) Map.empty
  print $ solve_2 (tail ops2) ((\(Mask m) -> m    ) $ head ops2) Map.empty