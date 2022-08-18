import React from "react";

const Button = ({ children, type = "button", className }) => {
  return (
    <>
      <button
        className={`${className} w-full my-2 py-1.5 px-2.5 border-solid text-white text-sm font-semibold rounded border-gray-300`}
        type={type}
        style={{ backgroundColor: "rgba(0,149,246,.3)" }}
      >
        {children}
      </button>
    </>
  );
};

export default Button;
