from hwfunction import get_target_files,concat_df,get_monthly_payment

def main():
    target_files = get_target_files("20")
    combined_df = concat_df(target_files)
    combined_df['monthly_payment'] = combined_df['comments'].apply(get_monthly_payment)
    combined_df.to_csv("final_result.csv")
    print("Done!!")


if __name__ == "__main__":
    main( )
    
    print "Added this line"