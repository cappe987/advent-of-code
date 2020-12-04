module Main where

import Data.List
import Data.List.Split
import Data.Char

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

parse = map (words . unwords) . splitOn [""]

solve_1 pass = 
  fromEnum $ all (\rq -> any (rq `isPrefixOf`) (filter (not . ("cid" `isPrefixOf`)) pass)) req
  
solve_2 pass = 
  fromEnum $ all (\rq -> any (rq `isPrefixOf`) ws) req && all isValid ws
  where ws = filter (not . ("cid" `isPrefixOf`)) pass

digitRange xs l u = 
  let val = (read xs :: Int) 
  in length (filter isDigit xs) == 4 && val >= l && val <= u

isValid ('b':'y':'r':':':xs) = digitRange xs 1920 2002
isValid ('i':'y':'r':':':xs) = digitRange xs 2010 2020
isValid ('e':'y':'r':':':xs) = digitRange xs 2020 2030
isValid ('h':'g':'t':':':xs) = 
  if "cm" `isSuffixOf` xs then
    (read (takeWhile isDigit xs) :: Int) `elem` [150..193]
  else 
    (read (takeWhile isDigit xs) :: Int) `elem` [59..76]
isValid ('h':'c':'l':':':xs) = head xs == '#' && all (`elem` ['0'..'9'] ++ ['a'..'f']) (tail xs)
isValid ('e':'c':'l':':':xs) = xs `elem` ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
isValid ('p':'i':'d':':':xs) = length (filter isDigit xs) == 9

main :: IO () 
main = do 
  input <- lines <$> readFile "input.txt"
  print $ sum $ map solve_1 (parse input)
  print $ sum $ map solve_2 (parse input)
