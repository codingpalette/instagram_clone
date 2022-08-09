import React from "react";

const Button = ({ children, type = "button", className }) => {
  return (
    <>
      <button
        className={`${className} py-1 px-2.5 border-solid border rounded border-gray-300`}
        type={type}
      >
        {children}
      </button>
    </>
  );
};

export default Button;
