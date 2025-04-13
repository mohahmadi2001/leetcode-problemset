// First solution
function longestCommonPrefix(strs: string[]): string {
  const prefixes: string[] = [];
  for (let i = 0; i < strs[0].length; i++) {
    prefixes.push(strs[0].slice(0, i + 1))
  }

  for (let i = prefixes.length - 1; i >= 0; i--) {
    if (strs.every(str => str.startsWith(prefixes[i]))) {
      return prefixes[i]
    }
  }

  return '';
};

// Second solution
function longestCommonPrefix2(strs: string[]): string {
  strs.sort();
  const firstItem = strs[0];
  const lastItem = strs[strs.length - 1];
  let result = '';

  for (let i = 0; i < firstItem.length; i++) {
    if (firstItem[i] !== lastItem[i]) {
      break;
    }

    result += firstItem[i];
  }

  return result;
};
