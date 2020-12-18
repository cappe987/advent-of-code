module Main where

import Data.Char
import Data.Bifunctor as Bf

precedence :: Char -> Int -- Change precedence level of + to 2 for part 1
precedence c = case c of '+' -> 3; '*' -> 2; '(' -> 1; ')' -> 1;

shouldPopStack :: Char -> Char -> Bool
shouldPopStack x top = precedence x <= precedence top && top /= '('

popWhile :: Char -> (String, String) -> (String, String)
popWhile c (out, []) = (out, []) 
popWhile c (out, x:stack) = 
  if shouldPopStack c x then popWhile c (x:out, stack) else (out, x:stack)

shunting :: String -> (String, String) -> String
shunting [] (out, stack) = reverse stack ++ out
shunting ('(':xs) (out, stack) = shunting xs (out, '(':stack)
shunting (')':xs) (out, stack) = 
  let (ops, rest) = span (/= '(') stack
  in shunting xs (reverse ops ++ out, tail rest)
shunting ('+':xs) yard = shunting xs (Bf.second ('+':) $ popWhile '+' yard)
shunting ('*':xs) yard = shunting xs (Bf.second ('*':) $ popWhile '*' yard)
shunting (x  :xs) (out, stack) = shunting xs (x:out, stack)

evalPostfix :: String -> (Int, String)
evalPostfix ('+':xs) = 
  let (left, rest)   = evalPostfix xs
  in Bf.first (left+) $ evalPostfix rest
evalPostfix ('*':xs) = 
  let (left, rest)  = evalPostfix xs
  in Bf.first (left*) $ evalPostfix rest
evalPostfix (x:xs) = (digitToInt x, xs)

main :: IO ()
main = do 
  input <- lines <$> readFile "input.txt"
  print $ sum $ map (\s -> fst $ evalPostfix $ shunting (filter (/= ' ') s) ([],[])) input