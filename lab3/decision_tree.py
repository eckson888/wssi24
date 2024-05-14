import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, x, y):
        self.n_features = x.shape[1] if not self.n_features else min(x.shape[1],self.n_features)
        self.root = self._grow_tree(x,y)

    def _grow_tree(self, x, y, depth=0):
        n_samples, n_feats = x.shape
        n_labels = len(np.unique(y))      
        if n_labels==1 or depth>=self.max_depth or n_samples<self.min_samples_split:
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
          
        feat_index = np.random.choice(n_feats, self.n_features, replace=False)
        best_threshold, best_feature = self._best_split(x,y,feat_index)
        left_indexes, right_indexes = self._split(x[:, best_feature], best_threshold)
        left = self._grow_tree(x[left_indexes, :], y[left_indexes], depth+1)
        right = self._grow_tree(x[right_indexes, :], y[right_indexes], depth+1)
        return Node(best_feature,best_threshold,left,right)

    def _best_split(self,x,y,feat_idxs):
        best_gain = -1
        split_index, split_threshold = None, None

        for feat_index in feat_idxs:
            x_column = x[:, feat_index]
            threshold = np.unique(x_column)
            for thr in threshold:
                gain = self._information_gain(y,x_column, thr)
                if best_gain<gain:
                    best_gain = gain
                    split_index = feat_index
                    split_threshold = thr
        return split_threshold, split_index

    def _information_gain(self, y, X_column, threshold):
        
        parent_entropy = self._entropy(y)
        
        left_indexes, right_indexes = self._split(X_column,threshold)
        if len(left_indexes) == 0 or len(right_indexes) == 0:
            return 0

        n = len(y)
        n_l, n_r = len(left_indexes), len(right_indexes)
        e_l, e_r = self._entropy(y[left_indexes]), self._entropy(y[right_indexes])
        child_entropy = (n_l/n)*e_l+(n_r/n)*e_r
        information_gain = parent_entropy - child_entropy
        return information_gain

    def _split(self, X_column, split_thresh):
        left_indexes = np.argwhere(X_column<split_thresh).flatten()
        right_indexes = np.argwhere(X_column>split_thresh).flatten()
        return left_indexes, right_indexes

    def _entropy(self, y):#x
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p*np.log(p) for p in ps if p>0])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x,node.right)

    def predict(self, X):#x
        return np.array([self._traverse_tree(x,self.root) for x in X])

    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value
