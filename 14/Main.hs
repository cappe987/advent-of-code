module Main where

import Data.Bits
import qualified Data.Map as Map

type Bitflip = Int -> Int
type Memory = Map.Map Int Int

data Op = Asn Int Int | Mask [Bitflip]

data Op2 = Asn2 Int Int | Mask2 Mask

type Mask = ([Bitflip], [Int -> [Int]]) 
-- Second is will be producing new values, not overwriting.


solve_1 :: [Op] -> [Bitflip] -> Memory -> Int
solve_1 [] _ mem = sum $ map snd $ Map.toList mem
solve_1 (Mask bflips : xs) _ mem = solve_1 xs bflips mem
solve_1 (Asn a b : xs) mask mem = 
  solve_1 xs mask (Map.insert a (foldl (\n f -> f n) b mask) mem)




parseMask :: Int -> String -> [Bitflip]
parseMask _ [] = []
parseMask pow ('0':xs) = (complement (2^pow) .&.) : parseMask (pow+1) xs
parseMask pow ('1':xs) = ((2^pow) .|.) : parseMask (pow+1) xs 
parseMask pow ('X':xs) = parseMask (pow+1) xs

writeFloating :: Int -> Int -> [Int]
writeFloating pow i = [complement (2^pow) .&. i, (2^pow) .|. i]

parseMask2 :: Int -> String -> Mask -> Mask
parseMask2 _   [] mask = mask
parseMask2 pow ('0':xs) mask = parseMask2 (pow+1) xs mask
parseMask2 pow ('1':xs) (a,b) = parseMask2 (pow+1) xs (((2^pow) .|.):a, b)
parseMask2 pow ('X':xs) (a,b) = parseMask2 (pow+1) xs (a, writeFloating pow : b)

parseOp :: String -> Op
parseOp s = 
  if head ws == "mask" then
    Mask $ parseMask 0 (reverse $ ws !! 2)
  else
    Asn (read $ takeWhile (/= ']') $ drop 4 (head ws)) (read (ws !! 2))
  where ws = words s

parseOp2 :: String -> Op2
parseOp2 s = 
  if head ws == "mask" then
    Mask2 $ parseMask2 0 (reverse $ ws !! 2) ([],[])
  else
    Asn2 (read $ takeWhile (/= ']') $ drop 4 (head ws)) (read (ws !! 2))
  where ws = words s



solve_2 :: [Op2] -> Mask -> Memory -> Int
solve_2 [] _ mem = sum $ map snd $ Map.toList mem
solve_2 (Mask2 mask : xs) _ mem = solve_2 xs mask mem
solve_2 (Asn2 a b   : xs) (bflips, floats) memory = 
  solve_2 xs (bflips, floats) $ foldl (\mem addr -> Map.insert addr b mem) memory addrs
  where addr = foldl (\n f -> f n) a bflips
        addrs = foldl (flip concatMap) [addr] floats

main :: IO ()
main = do 
  input <- map parseOp . lines <$> readFile "input.txt"
  print $ solve_1 (tail input) ((\(Mask xs) -> xs) $ head input) Map.empty

  input <- map parseOp2 . lines <$> readFile "input.txt"
  print $ solve_2 (tail input) ((\(Mask2 mask) -> mask) $ head input) Map.empty