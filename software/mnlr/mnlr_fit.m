function [model]=mnlr_fit(X, label, reg)
% MNLR_FIT  MultiNomial Logistic Regression Fitting
%   Usage:
%      [model] = MNLR_FIT(X, label, reg)
%   X is an N-by-M matrix of features, where each row is a data sample
%   label is an N-by-1 vector of data labels, where each element takes a
%       value from exactly 1,2,..,K
%   reg is the L2 regularization parameter, default 0
%   model is an (M+1)-by-(K-1) matrix, where the first row corresponds to
%       the bias term of each feature, and the the column corresponding to
%       the last feature is omitted to avoid over-parameterization. This
%       model is compatible with Matlab built-in function mnrfit and mnrval.
%
%   See also MNRFIT, MNRVAL.
%   Written by Peng Qi (qipeng.thu@gmail.com).
%   Last_update: Dec 29, 2012

    [N, M] = size(X);
    K = max(label);
    model = 0.01 * randn(M + 1, K - 1);
    
    if (nargin < 3),
        reg = 0;
    end
    options = optimset('GradObj','on','Display','none', 'MaxIter', 1e4, 'MaxFunEvals', 1e5);
    model = reshape(minFunc(@(model)target_fun(model, X, label, reg), model(:), options), M+1,K - 1);
end

function [f, g] = target_fun(model_, X, y, reg)
    [n,p] = size(X);
    k = max(y);
    X = [ones(n,1), X];
    p = p + 1;
    w = reshape(model_,[p k-1]);
    w(:,k) = zeros(p,1);

    Z = sum(exp(X*w),2);
    f = -sum((sum(X.*w(:,y).',2) - log(Z))) / n + reg / 2 * sum(sum(w(2:end,:).^2));

    if nargout > 1
        g = zeros(p,k-1);

        for c = 1:k-1
            g(:,c) = -sum(X.*repmat((y==c) - exp(X*w(:,c))./Z,[1 p]));
        end
        g = g / n;
        g(2:end,:) = g(2:end,:) + reg * w(2:end,1:end-1);
        g = g(:);
    end

end