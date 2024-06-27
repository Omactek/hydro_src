from django.db.models import Func

def prepare_data_for_chart(results): #prepares data for chart by modifying date strings and adding specific entries
    for result in results:
        month = result['string_date_without_year'][:2]
        result['string_date_without_year'] = f"{month}-15T00:00:00"

    # Find December and January results
    dec_result = next((result for result in results if result['string_date_without_year'].startswith('12-')), None)
    jan_result = next((result for result in results if result['string_date_without_year'].startswith('01-')), None)

    # Add December previous year as '01-01T00:00:00'
    if dec_result:
        dec_result_prev_year = dec_result.copy()
        dec_result_prev_year['string_date_without_year'] = '01-01T00:00:00'
        results.insert(0, dec_result_prev_year)

    # Add January next year as '12-31T00:00:00'
    if jan_result:
        jan_result_next_year = jan_result.copy()
        jan_result_next_year['string_date_without_year'] = '12-31T00:00:00'
        results.append(jan_result_next_year)

    return results