module Main where

import qualified Data.IntMap.Strict as Map

solve :: Int -> Map.IntMap Int -> Int -> Int -> Int
solve limit mem t prev 
  | t == limit = prev
  | otherwise =
    case Map.lookup prev mem of
      Nothing -> solve limit (Map.insert prev (t-1) mem) (t+1) 0
      Just t' -> solve limit (Map.insert prev (t-1) mem) (t+1) (t-t'-1)

main = do 
  let input = [20,0,1,11,6,3] -- 436
      initMemory = Map.fromList $ zip  (init input) [1..]

  print $ solve 2021 initMemory (length input+1) (last input)
  print $ solve 30000001 initMemory (length input+1) (last input)
  -- Runtime about 50s for part 2.