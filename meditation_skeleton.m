%% Loading data and initializing variables
path = "test.xdf";                                      % Load stream
data = load_xdf(path); 
medi = data{1,2}.time_series(1,:);                      % Grabbing mediation measure from XDF
s_rate = 512;                                           % Sample rate in Hz
wind_sze = 10;                                          % Window size we are averaging in seconds
overlap = 5;                                            % Overlapping windows in seconds
avgs = [];                                              % List of averages
%% Loop to find average of intervals
loop = 0;  
measure = 0;
while data                                              % Not sure how to begin while loop
    % Fill in code to take measure everyone 5 secs and can possible do
    % more measures for accuracy (i.e. 2.5 secs, 2 secs)
    data_end = length(meditation);                      % End at the most recent data point
    data_start = data_end - (wnd_sze * s_rate);         % Start at 10secs before with sample rate involved
    interval = meditation(data_start : data_end);       % The interval of window
    avgs(loop) = mean(interval);                        % Finding the average and putting them in a list
    loop = loop + 1;                                    % Creating new values of avgs
    avg_end = length(avgs);                             % Get length of 'avgs' to get most recent measure
    measure = mean(avgs(avg_end - 1) + avg(avg_end));   % Mean of most recent and measure before
end
%% Loop find overlap averages and final measure
if measure >= x
    disp('+2')
else
    disp('-2')
end
    