{-# LANGUAGE OverloadedStrings #-}
module Main where


import qualified Data.Map as Map
import qualified Data.Text as T
import Data.List
import Data.Maybe
import Data.Char
import Debug.Trace
import qualified Data.Set as S


type Side = [S.Set Int]
data Square = Square Int Side [Int]
  deriving Show


parseSquare :: [T.Text] -> Square
parseSquare ss = 
  Square id [top, bot, left, right] []
  where id = read $ T.unpack $ T.takeWhile isDigit $ T.drop 5 $ head ss :: Int
        image = tail ss
        top   = S.fromList $ map fst $ filter (\(_,c) -> c == '#') $  zip [0..] $ T.unpack $ head image
        bot   = S.fromList $ map fst $ filter (\(_,c) -> c == '#') $  zip [0..] $ T.unpack $ last image
        left  = S.fromList $ map fst $ filter (\(_,c) -> c == '#') $  zip [0..] $ map T.head image
        right = S.fromList $ map fst $ filter (\(_,c) -> c == '#') $  zip [0..] $ map T.last image


findMatch :: Square -> Square -> Bool 
findMatch (Square id sides m) (Square id' sides' m') =
  let allowFlip = sides ++  map (S.map (9 -)) sides
  in (id /= id') && any (`elem` sides') allowFlip 

countMatches :: [Square] -> [Square]
countMatches xs = 
  map (\sq@(Square id sides ms) -> Square id sides (matches sq xs)) xs
  where matches :: Square -> [Square] -> [Int]
        matches sq = map (\(Square id _ _) -> id) . filter (findMatch sq) 

solve_1 :: [Square] -> Int
solve_1 = 
  product . map (\(Square id _ _) -> id) . filter (\(Square _ _ ms) -> length ms == 2) .  countMatches

main :: IO ()
main = do 
  input <- fmap (parseSquare . T.lines) . T.splitOn "\n\n" . T.pack <$> readFile "input.txt"

  print $ solve_1 input

