class Solution {
    public boolean hasDuplicate(int[] nums) {
        int flag = 0;
        Set<Integer> unique =  new HashSet<>();
        for(int i = 0; i<nums.length; i++){
            if(unique.contains(nums[i])){
                flag = flag + 1;
            }
            unique.add(nums[i]);
        }
    if (flag == 0){
        return false;
    }
    else {
        return true;
    }
    }
}