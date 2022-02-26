#include <cstdlib>

class MedianFinder {
public:
    /** initialize your data structure here. */
    multiset<int> s1;
	multiset<int> s2;
    
    MedianFinder() {
	    s1.clear();
        s2.clear();
    }
    
    void addNum(int x) {
        //Adding Number to first set only if its empty or if number less than max element of set 1
        if(s1.size()==0||x<*(prev(s1.end()))){
	        s1.insert(x);
	    }
	    else s2.insert(x);
        //Adjusting sizes so that difference is never greater than 1
	    if(abs(int(s1.size()-s2.size()))>1){
	        if(s1.size()>s2.size()){
	            s2.insert(*(prev(s1.end())));
	            s1.erase(prev(s1.end()));
	        }
	        else{
	            s1.insert(*(s2.begin()));
	            s2.erase(s2.begin());
	        }
	    }
    }
    
    double findMedian() {
        double med;
        //check if odd or even number of elements
        if(abs(int(s1.size()-s2.size()))>0){
	        if(s1.size()>s2.size()){
	            med=*(prev(s1.end()));
	        }
	        else
	            med=*(s2.begin());
	    }
	    else {
	        med=0.5*(*(prev(s1.end()))+*(s2.begin()));
	    }
        return med;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */