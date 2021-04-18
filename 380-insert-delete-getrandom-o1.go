package main

type RandomizedSet struct {
	m map[int]struct{}
}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	p := make(map[int]struct{})
	return RandomizedSet{p}
}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.m[val]; ok{
		return false
	}
	this.m[val] = struct{}{}
	return true
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.m[val]; ok{
		delete(this.m, val)
		return true
	}
	return false
}


/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	for key, _ := range this.m{
		return key
	}
	return 0
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */

func main(){

}