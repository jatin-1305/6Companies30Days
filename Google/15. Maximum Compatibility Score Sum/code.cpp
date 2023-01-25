class Solution {
public:

    int get_score(vector<vector<int>>& students, vector<vector<int>>& mentors,int i,int j){
        int match = 0;
        for(int k=0;k<students[0].size();k++){
            if(students[i][k]==mentors[j][k]) match++;
        }
        return match;
    }

    int solve(vector<vector<int>>& students, vector<vector<int>>& mentors,int idx, vector<int> s){
        if(idx==students.size()){
            return 0;
        }
        int max_score = INT_MIN;
        for(int i=0;i<mentors.size();i++){
            if(s[i]==0){
                s[i] = 1;   
                max_score = max(max_score,solve(students,mentors,idx+1,s)+get_score(students,mentors,idx,i));
                s[i] = 0;
            }
        }
        return max_score;
    }

    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        vector<int> s(mentors.size(),0);
        return solve(students, mentors, 0, s);
    }
};
