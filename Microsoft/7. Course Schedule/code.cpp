class Solution {
public:
    bool canFinish(int v, vector<vector<int>>& prerequisites) {
        vector<int> adj[v];
        for(auto x: prerequisites) {
            vector<int> data = x;
            int a=data[0];
            int b=data[1];
            adj[a].push_back(b);
        }
        vector<int>indegree(v,0);
        vector<int>topo;
        for(int i=0;i<v;i++) {
            vector<int>data = adj[i];
            for(auto j: data){
                indegree[j]++;
            }
        }
        queue<int>q;
        for(int i=0;i<v;i++){
            if(indegree[i]==0) q.push(i);
        }
        while(!q.empty()) {
            int top = q.front();
            q.pop();
            topo.push_back(top);
            for(auto x: adj[top]){
                indegree[x]--;
                if(indegree[x]==0) q.push(x);
            }
        }
        return topo.size()==v;
    }
};
