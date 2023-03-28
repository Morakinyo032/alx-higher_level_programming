#!/usr/bin/python3
class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        positions = [None]*n
        _, count = self.solve(n, 0, positions, count=0)
        return count


    def solve(self, n, curr_row, positions, count):
        """
        Returns a tuple where the first element denotes whether there's a solution or not (Boolean) while
        the second element keeps track of the count (of unique solutions).
        """
        if curr_row == n:
            count += 1             # Update the count.
            return (False, count)  # This is set to False to ensure that the search continues even after finding a unique solution.
        else:
            # Loop through all possible columns (of "curr_row") to check for valid solution.
            for curr_col in range(n):

                # Check if "curr_row" and "curr_col" are valid
                is_valid = True
                for prev_row in range(curr_row):
                    prev_col = positions[prev_row]
                    cond1 = prev_col == curr_col
                    cond2 = prev_col+prev_row == curr_col+curr_row
                    cond3 = prev_col-prev_row == curr_col-curr_row
                    if cond1 or cond2 or cond3:
                        is_valid = False
                        break
                # End of for loop.

                # If "curr_row" and "curr_col" are valid...
                if is_valid:
                    positions[curr_row] = curr_col

                    # Recursive part. Check if next row is valid.
                    # If next row is True (or valid), return True (to the previously called function or previous row)
                    can_solve, count = self.solve(n, curr_row+1, positions, count)
                    if can_solve is True:
                        return (can_solve, count)
            # End of for loop on columns.

            # We have looped through all the possible columns and cannot find any solution.
            # Let the previously called function know that there is no solution.
            return (False, count)

        # End of if/else statement.
