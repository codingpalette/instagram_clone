import React from "react";

const Input = ({
  type,
  placeholder,
  className,
  maxLength,
  style,
  defaultValue,
  id,
  register,
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
        {...register}
      />
    </>
  );
};

export default Input;
