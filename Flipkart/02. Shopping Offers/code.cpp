class Solution {
public:
    bool can_take_offer(vector<int> &off , vector<int> &need)
    {
        int n = need.size();
        for( int i = 0 ; i < n ; ++i )
        {
            if( off[i] > need[i] )
            return false;
        }
        return true;
    }
    
    int fun( int ind , vector<int> &needs , vector<vector<int>> &special ,vector<int> &price)
    {
        if( ind == -1 ) // single offer  
        {
            int sum = 0 ;
            for( int i = 0 ; i  < needs.size() ; ++i )
            {
                sum += ( needs[i] * price[i]);
            }
            return sum ;

        }

        int nottake = fun(ind-1,needs,special,price);
        int take = 1e9;
        if( can_take_offer(special[ind] ,needs))
        {   
            for( int i  = 0 ; i < needs.size() ; ++i )
            {
                needs[i] -= (special[ind][i]);
            }
            take = special[ind][needs.size()] + fun(ind , needs,special,price);
             for( int i  = 0 ; i < needs.size() ; ++i )
            {
                needs[i] += (special[ind][i]);
            }
           
        }
        return min(take,nottake);

    }
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int n = needs.size();    
        return fun(special.size()-1 , needs,special,price);      
    }
};
