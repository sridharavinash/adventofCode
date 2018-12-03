defmodule Day1 do
    def readFile(filename) do
        File.stream!(filename)
            |> Stream.map(fn line ->
                {integer,_} = Integer.parse(line)
                integer
             end)
            |> Enum.sum()
    end
end

Day1.readFile("input.txt")
    |> IO.inspect