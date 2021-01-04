

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *ans;
    ans = (int*)malloc(2*sizeof(*ans));
    *returnSize = 2;
    if (ans != NULL) { // check pointer isn't null
        
        for (int i = 0; i < numsSize; i++) {
          for (int j = 1 + i; j < numsSize; j++) {
              
              if (*(nums+i) + *(nums+j) == target) {
                    *ans = i;
                    printf("%d, %d", i, j);
                    *(ans+1) = j;
                }
            }
        }
    }
    
    return ans;
}