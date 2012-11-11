function semilogxBar(x, y, c)
% SEMILOGXBAR  Draws bar plot on a semilogx axis
%       SEMILOGXBAR(x,y) with x indicating the centers of the bars, and y
%           indicating the values of the bars
%       SEMILOGXBAR(x,y,c) with c indicating the bar color. Both
%          single-char string form ('r', 'g', 'b', etc) and vector form 
%          [r g b] are accepted. See FILL for more information on colors.
%       This function changes the current gca to semilogx scale. For loglog
%       bar plot, try SET(gca,'YScale','log').
%
%   Written by Peng Qi, Nov 11, 2012. qipeng.thu@gmail.com

if nargin<3,
    c='b';
end
x = log(x);
interv = 1;
if (length(x)>=2), interv=(x(2)-x(1))/2;end
if gca == 0,
    figure;
end
washold = ishold;
if ~washold, hold on;end
base = zeros(1,length(x)+1);
base(1) = exp(x(1)-interv);
for i = 1:length(x),
    base(i+1) = exp(x(i)+interv);
end
for i = 1:length(x),
    rectangle('Position', [base(i) 0 base(i+1)-base(i) y(i)]);
    fill([base(i) base(i+1) base(i+1) base(i)], [0 0 y(i) y(i)], c);
end
if ~washold,hold off;end
set(gca,'XScale','log');
end