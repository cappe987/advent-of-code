{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TupleSections #-}
module Main where

import Data.List
import Data.Maybe
import qualified Data.Text as T
import Data.Char
import Debug.Trace
import Data.Bifunctor as Bf



data Field = Field String [Int -> Bool]
type Ticket = [Int]
type TicketWId = [(Int, Int)]

--------------------- Part 1 -----------------
solve_1 :: [Int -> Bool] -> [Ticket] -> Int
solve_1 fs =
   foldr ((+) . foldl (\acc n -> if any (\f -> f n) fs then acc else acc+n) 0) 0 


--------------------- Part 2 -----------------
-- Discards the invalid fields from part 1
discardInvalid :: [Int -> Bool] -> [Ticket] -> [Ticket]
discardInvalid fs = filter (all (\x -> any (\f -> f x) fs))

-- Finds which id's a field can be, for a specific ticket
findValidIdForField :: [Int -> Bool] -> TicketWId -> [Int]
findValidIdForField [f1, f2] = 
  map fst . filter (\(i,n) -> f1 n || f2 n)

-- Removes valid id's from a field in case another ticket invalidated that id
removeInvalidIds :: (Field, [Int]) -> TicketWId -> (Field, [Int])
removeInvalidIds (fl@(Field n fs), xs) ticket = 
  (fl, xs `intersect` findValidIdForField fs ticket)

-- Finds the valid id's for a field
findTicketFields :: [(Field, [Int])] -> TicketWId -> [(Field, [Int])]
findTicketFields fields ticket = map (`removeInvalidIds` ticket) fields

-- findFields maps each field to which id's they can go to
findFields :: [(Field, [Int])] -> [TicketWId] -> [(String, [Int])]
findFields fls ts = map (\(Field n _, i) -> (n,i)) $ foldl findTicketFields fls ts

-- assignFields will whittle down the id's that a field can go to, 
-- until all fields have been assigned an id.
assignFields :: [(String, [Int])] -> [(String, Int)]
assignFields fields = 
  reduce sorted
  where sorted = sortBy (\(_, xs) (_,ys) -> compare (length xs) (length ys)) fields
        reduce :: [(String, [Int])] -> [(String, Int)]
        reduce [] = []
        reduce ((n,[x]):xs) = (n,x) : reduce (map (Bf.second (filter (/= x))) xs)


-- multiplyDeparture finds the final answer.
multiplyDeparture :: TicketWId -> [(String, Int)] -> Int
multiplyDeparture myticket fields = 
  product $ map snd $ filter (\(i,v) -> i `elem` depFields) myticket
  where depFields = map snd $ filter (\(n,_) -> "departure" `isPrefixOf` n) fields

solve_2 :: [Field] -> Ticket -> [Ticket] -> Int 
solve_2 fieldreqs myticket tickets = 
  let valids = discardInvalid (concatMap (\(Field _ fs) -> fs) fieldreqs) tickets
      withId = map (zip [0..]) valids :: [TicketWId]
      reqsWIds = map (, [0..length (head valids) -1]) fieldreqs :: [(Field, [Int])]

  in multiplyDeparture (zip [0..] myticket) $ assignFields $ findFields reqsWIds withId



--------------------- Main & parsing -----------------

parseTicket :: T.Text -> [Int]
parseTicket = map ((read :: String -> Int) . T.unpack) . T.splitOn ","

parseFieldReq :: T.Text -> Field
parseFieldReq s = 
  Field (T.unpack name) reqF
  where (name, rest) = T.span (/= ':') s
        reqs = T.splitOn " or " $ T.drop 2 rest
        reqF = map 
          (\s -> let [l,u] = T.splitOn "-" s in \n -> n >= read (T.unpack l) && n <= read (T.unpack u)) reqs

parse :: [T.Text] -> ([Field], Ticket, [Ticket])
parse ss = 
  (map parseFieldReq fields, myticket, othertickets)
  where (fields, rest) = span (/= "") ss
        myticket = parseTicket $ rest !! 2
        othertickets = map parseTicket $ drop 5 rest


main :: IO ()
main = do 
  (fieldreqs, myticket, tickets) <- parse . T.lines . T.pack <$> readFile "input.txt"

  print $ solve_1 (concatMap (\(Field _ fs) -> fs) fieldreqs) tickets
  print $ solve_2 fieldreqs myticket tickets