/*
Example Input: nums = [2,7,11,15], target = 9
Example Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

let nums = [2,7,11,15,9];
const target = 9;
var twoSum = function(nums, target) {
  for (let index = 0; index < nums.length; index++) {
    for (let next_index = index + 1; next_index < nums.length; next_index++) {
      if(nums[index] + nums[next_index] === target) {
        return [index, next_index]
      }
    }
  }
};

console.log(twoSum(nums, target));
