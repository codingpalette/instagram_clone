import React, { Children } from "react";

const Input = ({
  children,
  type,
  placeholder,
  className,
  maxLength,
  style,
  defaultValue,
  id,
}) => {
  return (
    <>
      <input
        type={type}
        placeholder={placeholder}
        className={`${className} w-full border border-gray-200 rounded-sm text-xs focus:outline-none focus:border-gray-400`}
        maxLength={maxLength}
        style={style}
        defaultValue={defaultValue}
        id={id}
      >
        {children}
      </input>
    </>
  );
};

export default Input;
