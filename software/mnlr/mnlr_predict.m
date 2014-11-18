function [y] = mnlr_predict(model, X, outputLabel)
% MNLR_PREDICT  MultiNomial Logistic Regression Prediction
%   Usage:
%      [y] = MNLR_PREDICT(model, X, outputLabel)
%   model is an (M+1)-by-(K-1) matrix, where the first row corresponds to
%       the bias term of each feature, and the the column corresponding to
%       the last feature is omitted to avoid over-parameterization. This
%       model is compatible with Matlab built-in function mnrfit and mnrval.
%   X is an N-by-M matrix of features, where each row is a data sample
%
%   By default, the output is the same as Matlab built-in function mnrval,
%   that is, an N-by-K matrix of probabilities that each data sample is
%   classified into a class. If outputLabel present (whatever its value),
%   the output will be a vector of labels instead, which range from 1,2,...K.
%
%   See also MNRFIT, MNRVAL.
%   Written by Peng Qi (qipeng.thu@gmail.com).
%   Last_update: Dec 29, 2012

    y = mnrval(model, X);
    
    if nargin > 2,
        [~, y] = max(y, [], 2);
    end
end